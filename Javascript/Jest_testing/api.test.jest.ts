import { describe, it, expect } from "@jest/globals";
import { TextEncoder } from "util";
import { MyLambdaClient } from "aws-sdk";
import { expectedData } from "./validateData";

const LambdaClient = new MyLambdaClient();

describe("lambda fcn client-config-svc", () => {
  it("GET /api/clients can respond", async () => {
    //Arrange
    const data = new TextEncoder().encode(
      JSON.stringify({
        path: "/client-config-svc//api/clients",
        httpMethod: "GET",
      })
    );
    const expected = ["niagara-wineries"];
    const notExpected = ["testName1", "testName2"];

    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });

    //Assert
    expect(response.statusCode).toBe(200);
    expect(typeof response.body).toBe(Array);
    expect(response.body).toEqual(expect.arrayContaining(expected));
    expect(response.body).not.toEqual(expect.arrayContaining(notExpected));
  });

  it("GET /api/clients/{clientName} can respond", async () => {
    //Arrange
    const clientID = "niagara-wineries";
    const data = new TextEncoder().encode(
      JSON.stringify({
        path: `/client-config-svc/api/clients/${clientID}`,
        httpMethod: "GET",
      })
    );
    const expected = expectedData.clients.niagaraWinery;
    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });
    //Assert
    expect(response.statusCode).toBe(200);
    expect(response.body).toHaveProperty("clientID");
    expect(response.body.clientID).toEqual(expected.clientID);
    expect(response.body).toHaveProperty("clientName");
    expect(response.body.clientName).toEqual(expected.clientName);
    expect(response.body).toHaveProperty("brand");
    expect(response.body.brand).toEqual(expected.brand);
    expect(response.body).toHaveProperty("industry");
    expect(response.body.industry).toEqual(expected.industry);
    expect(response.body).toHaveProperty("status");
    expect(response.body.status).toEqual(expected.status);
    expect(response.body).toHaveProperty("country");
    expect(response.body.country).toEqual(expected.country);
  });

  it("GET /api/providers/ can respond", async () => {
    //Arrange
    const data = new TextEncoder().encode(
      JSON.stringify({
        path: `/client-config-svc/api/providers/`,
        httpMethod: "GET",
      })
    );
    const expected = ["semrush", "wine-expo"];
    const notExpected = ["testProvider1", "testProvider2"];
    //Act
    const response = await LambdaClient.invoke({
      FunctionName: "client-config-svc",
      payload: data,
    });
    //Assert
    expect(response.statusCode).toBe(200);
    expect(typeof response.body).toBe(Array);
    expect(response.body).toEqual(expect.arrayContaining(expected));
    expect(response.body).not.toEqual(expect.arrayContaining(notExpected));
  });

  const providerList = ["wine-expo", "facebook", "semrush"];
  const toDoProviderList = [
    "googleanalytics",
    "googletrends",
    "linkedin",
    "twitter",
  ];

  providerList.forEach((provider) => {
    it(`GET /api/providers/${provider} can respond`, async () => {
      //Arrange
      const data = new TextEncoder().encode(
        JSON.stringify({
          path: `/client-config-svc/api/providers/${provider}`,
          httpMethod: "GET",
        })
      );

      //Act
      const response = await LambdaClient.invoke({
        FunctionName: "client-config-svc",
        payload: data,
      });

      //Assert
      expect(response.statusCode).toBe(200);
      expect(typeof response.body).toBe(Array);
      expect(response.statusCode).toBe(200);
      expect(response.body).toHaveProperty("providerID");
      expect(response.body.providerID).toEqual(provider);
      expect(response.body).toHaveProperty("name");
      expect(response.body).toHaveProperty("clientID");
      expect(response.body).toHaveProperty("type");
      expect(response.body).toHaveProperty("granularity");
      expect(response.body).toHaveProperty("status");
      expect(response.body).toHaveProperty("isCustom");
      expect(response.body).toHaveProperty("domain");
      expect(response.body).toHaveProperty("resources");
      expect(response.body).toHaveProperty("historicalPullInMonths");
      expect(typeof response.body.historicalPullInMonths).toBe(Number);
    });
  });
});
